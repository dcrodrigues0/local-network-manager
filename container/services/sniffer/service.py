from werkzeug.exceptions import abort

import container.helper.table_formatter as formatter
import container.helper.graph as graph
from container.services.dbutils import mongo
import operator

class Service(mongo.MongoDAO):
    def __init__(self):
        mongo.MongoDAO.__init__(self)

    def getTrafficByDate(self, date, exibition, subtitle):
        return graph.makeDataGraph(self.getTrafficByDay(date), 'date', 'avg', exibition, subtitle)

    def getTrafficHourByDate(self, date, exibition, subtitle):
        return graph.makeDataGraph(self.getTrafficHour(date), 'hour', 'quantidade_pacotes', exibition, subtitle)

    def getRealTimeService(self, exibition, subtitle):
        return graph.makeDataGraph(self.getRealTime(), "min", "quantidade_pacotes", exibition, subtitle)

    def getRealTimeTrafficTableService(self, **Kwargs):
        filter_args = formatter.formatFilterArguments(Kwargs)
        date_args = formatter.formatDateArguments(Kwargs)
        limit = formatter.formatLimitArgument(Kwargs["limit"])

        return formatter.formatTableData(self.getRealTimeTrafficTable(filter_args, date_args, limit))

    def getTrafficByMacAddress(self, date, exibition, subtitle):
        return graph.makeDataGraph(self.getTrafficMac(date), 'mac_origem', 'quantidade_pacotes', exibition, subtitle)

    def getTrafficByRange(self, start, end, exibition, subtitle):

        start = start.split("-")
        end = end.split("-")

        contentField = self.getTrafficBetween()
        traffic = []

        for content in contentField:
            if content["date"].split("-")[1] >= start[1] and content["date"].split("-")[1] <= end[1]:
                if content["date"].split("-")[0] >= start[0] and content["date"].split("-")[0] <= end[0]:
                    traffic.append(content)

        return graph.makeDataGraph(traffic, 'date', 'quantidade_pacotes', exibition, subtitle)

    def getTrafficIp(self, date, hour, direction, exibition, subtitle):
        return graph.makeDataIpGraph(self.getTrafficIpAddress(date, hour), direction, exibition, subtitle)

    def getHighestIpTrafficByHour(self, date, hour, exibition, subtitle):
        dataset = None
        resultset = self.getMostTrafficHour(date, hour)

        if resultset.count() == 0: return abort(404)

        for result in self.getMostTrafficHour(date, hour):
            dataset = result

        dataset["ips"].sort(key=operator.itemgetter('size'), reverse=True)

        return graph.makeDataSubGraph(dataset["ips"][:5], exibition, subtitle)

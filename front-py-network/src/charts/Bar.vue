<script>
import { HorizontalBar } from 'vue-chartjs'

export default {
  extends: HorizontalBar,
  data: () => ({
    type: 'horizontalBar',
    chartdata: {
      labels: ['January', 'February'],
      datasets: [
            {
              label: 'Data One',
              backgroundColor: '#f87979',
              data: [40, 40]
            },
            {
              label: 'ta Foda',
              backgroundColor: 'gray',
              data: [30, 60]
            },
            {
              label: 'fuck',
              backgroundColor: 'red',
              data: [50, 35]
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
  }),

  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}

</script>
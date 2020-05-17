<template>
    <div class="content">
      <div class="graphs row">
        <Realtime class="col-md-6 col-12 mt-3" id='fuck' widthProp="100%" heightProp="300px" title="Consumo de pacotes realtime por minuto"/>
        <ChartByRangeDate class="col-md-6 col-12 mt-3" id='fuck' widthProp="100%" heightProp="300px" title="Consumo de pacotes por data início/fim"/>        
        <ChartPackageByHour class="col-md-6 col-12 mt-3" id='fuck' widthProp="100%" heightProp="300px" title="Pacotes consumidos por hora"/>
        <ChartByIpAddress class="col-md-6 col-12 mt-3" id='fuck' widthProp="100%" heightProp="300px" title="Envio de pacotes por IP de origem"/>
        <ChartByIpAddressDestination class="col-md-6 col-12 mt-3" id='fuck' widthProp="100%" heightProp="300px" title="Pacotes recebidos por IP de destino"/>
      </div>
    </div>
</template>

<script>
  import ChartPackageByHour from '@/tools/ChartPackageByHour';
  import Realtime from '@/tools/Realtime';
  import ChartByRangeDate from '@/tools/ChartByRangeDate'
  import ChartByIpAddress from '@/tools/ChartByIpAddress'
  import ChartByIpAddressDestination from '@/tools/ChartByIpAddressDestination'

  export default {
    name: 'view1',
    components: {
      'ChartPackageByHour':ChartPackageByHour,
      'Realtime':Realtime,
      'ChartByRangeDate':ChartByRangeDate,
      'ChartByIpAddress':ChartByIpAddress,
      'ChartByIpAddressDestination': ChartByIpAddressDestination
    }
  }

</script>
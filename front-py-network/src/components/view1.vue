<template>
    <div class="content">
      <div class="graphs row">
        <Bar class="col-md-6 col-12 mt-3" id='fuck' widthProp="100%" heightProp="300px" title="Consumo de pacotes por dia"/>
        <Realtime class="col-md-6 col-12 mt-3" id='fuck' widthProp="100%" heightProp="300px" title="Consumo de pacotes realtime por minuto"/>
        <ChartByRangeDate class="col-md-6 col-12 mt-3" id='fuck' widthProp="100%" heightProp="300px" title="Consumo de pacotes por data início/fim"/>        
      </div>
    </div>
</template>

<script>
  import Bar from '@/tools/Bar';
  import Realtime from '@/tools/Realtime';
  import ChartByRangeDate from '@/tools/ChartByRangeDate'
  export default {
    name: 'view1',
    components: {
      'Bar': Bar,
      'Realtime':Realtime,
      'ChartByRangeDate':ChartByRangeDate
    }
  }

</script>
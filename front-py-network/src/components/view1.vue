<template>
    <div class="content p-md-5 p-3">
      <div class="graphs row">
        <Realtime class="col-md-6 col-12 mt-3" id='fuck' isModal="false" widthProp="100%" heightProp="300px" title="Consumo de pacotes realtime por minuto"/>
        <ChartByRangeDate class="col-md-6 col-12 mt-3" id='fuck' isModal="false" widthProp="100%" heightProp="300px" title="Consumo de pacotes por data início/fim"/>        
        <ChartPackageByHour class="col-md-6 col-12 mt-3" id='fuck' isModal="false" widthProp="100%" heightProp="300px" title="Pacotes consumidos por hora"/>
        <ChartByIpAddressDestination class="col-md-6 col-12 mt-3" id='fuck' isModal="false" widthProp="100%" heightProp="300px" title="Pacotes recebidos por IP de destino"/>
        <ChartByTrafficMac class="col-md-6 col-12 mt-3" id='fuck' isModal="false" widthProp="100%" heightProp="300px" title="Consumo de pacotes por MAC Address de origem"/>
      </div>
      <b-modal centered size="xl" id="my-modal">
          <template v-slot:default>
            <div>
              <Realtime v-if="chart === 'realtime'" class="col-12 mt-3" isModal="true" widthProp="100%" heightProp="80%" title="Consumo de pacotes realtime por minuto"/>
              <ChartByRangeDate v-else-if="chart === 'chart-range-date'" class="col-12 mt-3" isModal="true" widthProp="100%" heightProp="80%" title="Consumo de pacotes por data início/fim"/>
              <ChartPackageByHour v-else-if="chart === 'chart-package-hour'" class="col-12 mt-3" isModal="true" widthProp="100%" heightProp="80%" title="Pacotes consumidos por hora"/>
              <ChartByIpAddressDestination v-else-if="chart === 'chart-ip-address-d'" class="col-12 mt-3" isModal="true" widthProp="100%" heightProp="80%" title="Pacotes recebidos por IP de destino "/>
            </div>
          </template>
      </b-modal>
    </div>
</template>

<script>
  import ChartPackageByHour from '@/tools/ChartPackageByHour';
  import Realtime from '@/tools/Realtime';
  import ChartByRangeDate from '@/tools/ChartByRangeDate'
  import ChartByIpAddressDestination from '@/tools/ChartByIpAddressDestination'
  import ChartByTrafficMac from '@/tools/ChartByTrafficMac'

  export default {
    name: 'view1',
    components: {
      'ChartPackageByHour':ChartPackageByHour,
      'Realtime':Realtime,
      'ChartByRangeDate':ChartByRangeDate,
      'ChartByIpAddressDestination': ChartByIpAddressDestination,
      'ChartByTrafficMac': ChartByTrafficMac
    },

    data() {
      return {
        chart: ''
      }
    },

    mounted() {
      let obj = document.querySelectorAll('.zoom')
      obj.forEach(element => {
        element.addEventListener('click', event => {
          this.chart = event.target.id
          console.log(event.target);
          
        })
      })
      
    }
  }
</script>

<style>
 svg, path{
   pointer-events: none;
 }
</style>
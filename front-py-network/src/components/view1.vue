<template>
    <div class="content">
      <div class="graphs row">
        <Bar class="col-md-6 col-12 mt-3" id='fuck' widthProp="100%" heightProp="300px" title="Consumo de pacotes por dia"/>
        <Bar class="col-md-6 col-12 mt-3" widthProp="100%" heightProp="300px" title="Network use"/>
      </div>
    </div>
</template>

<script>
  import Bar from '@/tools/Bar'
  export default {
    name: 'view1',
    components: {
      'Bar': Bar
    }
  }

</script>
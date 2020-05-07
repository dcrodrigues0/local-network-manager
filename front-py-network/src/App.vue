<template>
  <div id="app">
    <Index/>
  </div>
</template>

<script>
  import Index from '@/view/index.vue'
  export default {
    name: 'app',
    components: {
      Index
  }

}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  

  box-sizing: border-box;
  margin: 0;
  padding: 0;
  height: 100%;
}
</style>
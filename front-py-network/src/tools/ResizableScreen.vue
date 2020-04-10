<template>
  <div :style="{'width':widthProp}" class="resizable-screen">
    <p class="title-graph">{{title}}</p>
  </div>
</template>

<script>
  export default {
    props: {
      widthProp: {
        type: String,
        required: true,
        default: "350px"
      },
      heightProp: {
        type: String,
        required: true,
        default: "150px"
      },
      title: {
        type: String,
        default: 'Favor colocar titulo :)'
      },

    },
  }

</script>



<style>

  .title-graph{
    margin: 5px;
    color: lightgray;
    font-weight: bold;
  }

   .resizable-screen{
       /*width: 300px;*/
       height: 150px;
       background-color: #212124;
       margin: 5px;
   }
</style>



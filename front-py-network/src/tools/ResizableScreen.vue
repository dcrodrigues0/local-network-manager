<template>
  <div class="root">
    <div v-bind:style="{'width':widthProp,'height':heightProp}" class="resizable-screen">
      <div class="tools-tab">
        <a title="Fechar gráfico" v-on:click="closeTab" href="#"><i class="far fa-window-close"></i></a>
        <a title="Maximizar gráfico" v-on:click="maximizeTab" href="#"><i class="far fa-window-restore"></i></a>
        <a title="Minimizar gráfico" v-on:click="minimizeTab" href="#"><i class="fas fa-window-minimize"></i></a>
        <p class="title-graph">{{ title }}</p>
      </div>
      <!--CHART BELOW PLEASE -->
      <!-- <Bar :chartdata="dataGraph" :options="{responsive: true, maintainAspectRatio:false}" /> -->
      <Graph :style="{'width': 90%+'%', 'height':85 + '%'}"/>
    </div>
    <div class="bottomBar"/>
  </div>
</template>

<script>
  import Graph from '../charts/Graph';

  export default {  
    methods: {
      closeTab: function () {
        if(event.target.tagName == "path"){
          let window = event.target.parentNode.parentNode.parentNode.parentNode
          window.style.display = "none"
        }else if(event.target.tagName == "svg"){
          let window = event.target.parentNode.parentNode.parentNode
          window.style.display = "none"
        }else if(event.target.tagName == "A"){
          let window = event.target.parentNode.parentNode
          window.style.display = "none"
        }
      },
      minimizeTab: function () {
        if(event.target.tagName == "path"){
          let window = event.target.parentNode.parentNode.parentNode.parentNode
          document.querySelector('.bottomBar').appendChild(window);
        }else if(event.target.tagName == "svg"){
          let window = event.target.parentNode.parentNode.parentNode
          document.querySelector('.bottomBar').appendChild(window);
        }else if(event.target.tagName == "A"){
          let window = event.target.parentNode.parentNode
          document.querySelector('.bottomBar').appendChild(window);
        }
      },
      maximizeTab: function (){
        if(event.target.tagName == "path"){
            let window = event.target.parentNode.parentNode.parentNode.parentNode
            document.querySelector('.root').appendChild(window);
          }else if(event.target.tagName == "svg"){
            let window = event.target.parentNode.parentNode.parentNode
            document.querySelector('.root').appendChild(window);
          }else if(event.target.tagName == "A"){
            let window = event.target.parentNode.parentNode
            document.querySelector('.root').appendChild(window);
          }
      },
      getWindowHeight() {
        this.windowHeight = document.documentElement.clientHeight;
      },
    },
    data () {
        return {
          windowHeight: 0,
          dataGraph: null,
        response: ""
      }
    },
    mounted() {
      this.$nextTick(function() {
        window.addEventListener('resize', this.getWindowHeight);
        //Init
        this.getWindowHeight()        
      });
    },
    components:{
      Graph
    },
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
  .root{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }

  .bottomBar{
    height: 13%;
    background-color: #000000;
    width: 100%;
    bottom: 10px;
    position: absolute;
    display: flex;
    flex-direction: row;
    padding:5px;
    border-radius: 15px;
  }

  .bottomBar div{
    border-radius: 10px;
    resize: none!important;
    width: 200px!important;
    z-index: 10;
    overflow: hidden;
    height: 50px;
  }

  .tools-tab{
    width: 100%;  
    height: 15px;
    margin-bottom: 15px;
    display: flex;
    flex-direction: row;
    padding-left: 2px;
  }

  .tools-tab a{
    padding: 4px;
    color: #9f9f9f;
  }

  .tools-tab a:hover{
    transition: 1s;
    transform: scale(1.1);
  }

  .tools-tab a:nth-child(1){
    color: lightcoral;
  }

  .tools-tab a:nth-child(2){
    color: lightgreen;
  }
  
  .tools-tab a:nth-child(3){
    color: lightblue;
  }


  .title-graph{
    margin: 5px;
    color: lightgray;
    font-weight: bold;
  }

   .resizable-screen{
    resize: both;
    overflow: auto;
    background-color: #212124;
    margin: 5px;
    position: relative;
   }

   .resizable-screen-minimized p{
    display: none;
   }

   ::-webkit-resizer{ 
      background-color:#212124!important; 
   }

   @media only screen and (max-width: 600px) {
     .resizable-screen{
        resize: none;
        margin: 5px;
    }



   } 
    
</style>



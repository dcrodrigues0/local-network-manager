<template>
  <div class="root">
    <div v-bind:style="{'width':widthProp,'height':heightProp}" class="resizable-screen">
      <div class="tools-tab">
        <a title="Fechar gráfico" v-on:click="closeTab" href="#"><i class="far fa-window-close"></i></a>
        <a title="Maximizar gráfico" v-on:click="maximizeTab" href="#"><i class="far fa-window-restore"></i></a>
        <a title="Minimizar gráfico" v-on:click="minimizeTab" href="#"><i class="fas fa-window-minimize"></i></a>
        <p class="title-graph">{{ title }}</p>
      </div>

      <div class="size-control">
        <a href="#" @click="zoomChart">
          <i class="fas fa-expand"></i>
        </a>
        <a href="#" @click="unzoomChart">
          <i class="far fa-minus-square"></i>        
        </a>
        <a href="#" @click="configChart">
          <i class="fas fa-tools"></i>
        </a>
      </div>
      <!--CHART BELOW PLEASE -->
      <!-- <Bar :chartdata="dataGraph" :options="{responsive: true, maintainAspectRatio:false}" /> -->
      <Graph :style="{'width': 90%+'%', 'height':85 + '%'}"/>
    </div>
  </div>
</template>

<script>
  import Graph from '@/charts/Graph';

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
          window.childNodes[1].style.display = 'none'
          
          window.parentNode.className = 'root'
          document.querySelector('.bottomBar').appendChild(window.parentNode);
        }else if(event.target.tagName == "svg"){
          let window = event.target.parentNode.parentNode.parentNode
          window.childNodes[1].style.display = 'none'

          window.parentNode.className = 'root'
          document.querySelector('.bottomBar').appendChild(window.parentNode);

        }else if(event.target.tagName == "A"){
          let window = event.target.parentNode.parentNode
          window.childNodes[1].style.display = 'none'

          window.parentNode.className = 'root'
          document.querySelector('.bottomBar').appendChild(window.parentNode);
        }
      },
      maximizeTab: function (){
        if(event.target.tagName == "path"){
            let window = event.target.parentNode.parentNode.parentNode.parentNode
            window.childNodes[1].style.display = 'flex'

            window.parentNode.className = 'root col-md-6 col-12 mt-3'
            document.querySelector('.graphs').appendChild(window.parentNode);
          }else if(event.target.tagName == "svg"){
            let window = event.target.parentNode.parentNode.parentNode
            window.childNodes[1].style.display = 'flex'
            window.parentNode.className = 'root col-md-6 col-12 mt-3'
            document.querySelector('.graphs').appendChild(window.parentNode);
          }else if(event.target.tagName == "A"){
            let window = event.target.parentNode.parentNode
            window.childNodes[1].style.display = 'flex'
            window.parentNode.className = 'root col-md-6 col-12 mt-3'
            document.querySelector('.graphs').appendChild(window.parentNode);
          }
      },
      
      zoomChart: function(){
        let obj = event.target.parentNode.parentNode.parentNode.parentNode;

        if( obj.className.indexOf('col') !== -1){          
          obj.className = 'root col-12 fullscreen mt-3'
        }else if(obj.className.indexOf('resizable-screen') !== -1){
          obj.parentNode.className = 'root col-12 fullscreen mt-3'
        }

      },

      unzoomChart: function(){
        let obj = event.target.parentNode.parentNode.parentNode.parentNode;

        if( obj.className.indexOf('col') !== -1){          
          obj.className = 'root col-12 col-md-6  normalscreen mt-3'

        }else if(obj.className.indexOf('resizable-screen') !== -1){
          obj.parentNode.className = 'root col-12 col-md-6  normalscreen mt-3'
        }

      },

      configChart: function(){
          if(event.target.tagName == "path"){
            let window = event.target.parentNode.parentNode.parentNode.parentNode
            let obj = document.createElement('ResizableScreen')
            window.parentNode.appendChild(obj);
          }else if(event.target.tagName == "svg"){
            let window = event.target.parentNode.parentNode.parentNode
            let obj = document.createElement('ResizableScreen')
            window.parentNode.appendChild(obj);          }else if(event.target.tagName == "A"){
            let window = event.target.parentNode.parentNode
            let obj = document.createElement('ResizableScreen')
            window.parentNode.appendChild(obj);
          }
      },
    },
    data () {
        return {
          dataGraph: null,
          response: ""
      }
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
    border-radius: 5px solid black;
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
    color: rgb(219, 216, 216);
    font-weight: bold;
  }

   .resizable-screen{
    background-color: rgba(27, 26, 26, 0.856);
    margin: 5px;
    position: relative;
  }

    
   .resizable-screen-minimized p{
    display: none;
   }


   @media only screen and (max-width: 600px) {
     .resizable-screen{
        resize: none;
        margin: 5px;
    }

   } 

   .size-control{
     display: flex;
     position: absolute;
     flex-direction: column;
     top: 0;
     right: 0;
     height: 100%;
     padding-top: 5px;
   }

   .size-control a{
     font-size:20px;
     margin-top: 5px;
     margin-right: 10px;
   }
    
    
</style>



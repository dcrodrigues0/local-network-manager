<template>
  <main>
    <div class="black left-accordion">
      <a href="#" v-on:click="hideMenu" class="main-icons icon-logo" id="hideMenu">
        <i id="icon-direction" class="fas fa-angle-double-left"></i>
      </a>
      <a title="MAC Statistics" href="#" class="main-icons">
        <i class="fas fa-chart-bar"></i>
      </a>
      <a title="My network package statistics" href="#" class="main-icons">
        <i class="fas fa-wifi"></i>
      </a>
      <a title="MAC Statistics" href="#" class="main-icons">
        <i class="fas fa-chart-pie"></i>
      </a>
    </div>
    <div class="content-graphs">
      <div class="graphs">
        <ResizableScreen widthProp="350px" heightProp="150px" title="MAC use"/>
        <ResizableScreen widthProp="350px" heightProp="150px" title="Network use"/>
        <ResizableScreen widthProp="350px" heightProp="150px" title="Trafic use"/>
        <ResizableScreen widthProp="350px" heightProp="150px" title="RAM use"/>
      </div>
    </div>
  </main>
</template>

<script>
  import ResizableScreen from '../tools/ResizableScreen'
  export default {
    methods: {
      hideMenu: function () {
        let leftMenu = document.querySelector(".left-accordion");
        let icon = document.querySelector("#icon-direction");
        if(leftMenu.id == "hidded"){
          leftMenu.classList.remove('hide-left-accordion');
          leftMenu.id = "";
          icon.classList.remove('fa-angle-double-right');
          icon.classList.add('fa-angle-double-left');

        }else{
          leftMenu.classList.add('hide-left-accordion');
          leftMenu.id = "hidded";
          icon.classList.remove('fa-angle-double-left');
          icon.classList.add('fa-angle-double-right');
        }
      }
    },
    name: 'app',
    components: {
      'ResizableScreen': ResizableScreen
    }
  }

</script>



<style>
   main{
     width: 100%;
     background-color: #161719;
     height: 720px;
     position: fixed;
     overflow:hidden;
   }

    .graphs {
     display: flex;
     flex-direction: row;
     flex-wrap: wrap;
     padding: 6%;
     margin-left: 60px;
   }

   .content-graphs{
     width: 100%;
     height: auto;
   }

  .left-accordion{
    transition: 1s;
    width: 70px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    position: fixed;
    float: left;
    box-shadow: 6px 0px 17px -4px rgba(0,0,0,0.56);
  }

  .hide-left-accordion{
    transition: 1s;
    width: 25px;
  }

  .hide-left-accordion a{
    box-shadow: 6px 0px 17px -4px rgba(0,0,0,0.56);
    font-size: 12px;
  }

  .left-accordion a:link{
    color: #9F9F9F!important;
  }

  .left-accordion a{
    padding: 10px;
    color:#9F9F9F;
  }

  .left-accordion a:hover{
    transform: scale(1.2);
    transition: 0.5s;
  }

  .main-icons{
    font-size: 32px;
    position: relative;
  }

  .icon-logo{
    position: absolute;
    top: 0;
    margin-top: 20px;
    color:#9f9f9f!important;
    font-size: 35px;
  }

  @media only screen and (max-width: 600px) {
     .graphs{
       margin-left: 0px;
     }
  }

</style>
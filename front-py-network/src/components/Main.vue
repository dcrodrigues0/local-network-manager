<template>
  <main>
    <div class="black left-accordion">
      <a href="#" class="main-icons icon-logo">
        <i class="fas fa-paragraph"></i>
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
    name: 'app',
    components: {
      'ResizableScreen': ResizableScreen
    }
  }

</script>



<style>
   main{
     width: 100%;
     height: 100vh;
     background-color: #161719;
   }

    .graphs {
     display: flex;
     flex-direction: row;
     flex-wrap: wrap;
     padding: 3%;
   }

   .content-graphs{
     width: 100%;
     height: auto;
   }

  .left-accordion{
    width: 70px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    float: left;
    box-shadow: 6px 0px 17px -4px rgba(0,0,0,0.56);
  }

  .left-accordion a:link{
    color: #9F9F9F!important;
  }

  .left-accordion a{
    padding: 10px;
    color:#9F9F9F;
  }

  .left-accordion a:hover{
    font-size: 36px;
    transition: 0.2s;
  }

  .main-icons{
    font-size: 32px;
    position: relative;
  }

  .icon-logo{
    position: absolute;
    top: 0;
    margin-top: 20px;
    color:#ffab00!important;
    font-size: 35px;
  }

  .icon-logo:hover{
    transform: rotate(-360deg);
    transition: 1s!important;
  }

</style>
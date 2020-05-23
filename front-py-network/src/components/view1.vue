<template>
    <main class="p-md-5 p-3">

        <router-view class="content">
        </router-view>

        <div class="bottomBar">
        </div>

        <div class="left-accordion">
            <a href="#" v-on:click="hideMenu" class="main-icons icon-logo" id="hideMenu">
              <i id="icon-direction" class="fas fa-angle-double-left"></i>
            </a>
            <router-link title="MAC Statistics" to="/" class="main-icons">
              <i class="fas fa-chart-bar"></i>
            </router-link>
            <router-link title="My network package statistics" to="/view1" class="main-icons">
              <i class="fas fa-wifi"></i>
            </router-link>
        </div>

    </main>
</template>


<script>
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
      },
    },
}
</script>


<style>

  body, html{
      height: 100%;
  }


  main{
      width: 100%;
      height: 100%!important;
      overflow-y: scroll;
      background-color:#1E1F1A;
      height: auto;
  }

  .content{
    margin-left: 70px;
  }

  .left-accordion{
    transition: width 1s;
    width: 70px;
    display: flex; 
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    position: fixed;
    background-color:  #03070A;
    left: 0;
    top: 0;
    box-shadow: 6px 0px 17px -4px rgba(0,0,0,0.56); 
  }

  .hide-left-accordion{
    transition: width 1s;
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
    transition: 1s;
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

  .menu-size{
    display: none;
  }

  .bottomBar{
    height: auto;
    background-color: #000000;
    width: 100%;
    left: 80px;
    bottom: 0;
    position: fixed;
    display: flex;
    flex-direction: row;
    padding:5px;
    border-radius: 15px;
    z-index: 1;
  }

  .bottomBar div{
    border-radius: 10px;
    resize: none!important;
    width: 200px!important;
    z-index: 10;
    overflow: hidden;
    height: 50px;
  }

  @media only screen and (max-width: 600px) {
     .graphs{
       margin-left: 0px;
     }
  }

  .modal-body{
    padding: 0!important;
  }

  .modal-body > div > .root{
    margin-top: 0!important;
    padding: 0!important;
  }

  .modal-body > div > .root > .resizable-screen{
    margin: 0!important;
  }

  .modal-header{
    display: none!important;
  }

  .modal-footer{
    display: none!important;
  }


</style>
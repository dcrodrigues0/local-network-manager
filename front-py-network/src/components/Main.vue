<template>
  <div>
    <div id="rightBar" class="rightBar mainView">
      <div class="closeFilter">
        <a v-on:click="closeTab()" href="#" class="closeTab">
          <i class="fas fa-times"></i>
        </a>
      </div>
      <br/>
      <br/>
      <b-form  @submit="submit" class="row">

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="IP - Origem"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="Source-IP"
            class="mb-0">
            <b-form-input id="Source-IP" name="src-ip" placeholder="192.168.0.1">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Porta - Origem"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="Source-Port"
            class="mb-0">
            <b-form-input id="Source-Port" name="src-port" placeholder="80">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Mín. Porta - Origem"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="Start-source-port"
            class="mb-0">
            <b-form-input id="Start-source-port" name="start-src-port" placeholder="1">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Máx. Porta - Origem"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="End-source-port"
            class="mb-0">
            <b-form-input id="End-source-port" name="end-src-port" placeholder="65535">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="IP - Destino"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="Destination-IP"
            class="mb-0">
            <b-form-input id="Destination-IP" name="dst-ip" placeholder="192.168.0.1">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Porta - Destino"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="Destination-Port"
            class="mb-0">
            <b-form-input id="Destination-Port" name="dst-port" placeholder="80">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Mín. Porta - Destino"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="Start-destination-Port"
            class="mb-0">
            <b-form-input id="Start-destination-Port" name="start-dst-port" placeholder="1">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Máx. Porta - Destino"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="End-destination-Port"
            class="mb-0">
            <b-form-input id="End-destination-Port" name="end-dst-port" placeholder="65535">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Protocolo"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="Protocol"
            class="mb-0">
            <b-form-input id="Protocol" name="protocol" placeholder="Ex: TCP">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Mín. Comprimento"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="Length"
            class="mb-0">
            <b-form-input id="Length" name="start-length" placeholder="0">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Máx. Comprimento"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="Length"
            class="mb-0">
            <b-form-input id="Length" name="end-length" placeholder="1000">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Mín. TTL"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="ttl"
            class="mb-0">
            <b-form-input id="ttl" name="start-ttl" placeholder="0">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Máx. TTL"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="ttl"
            class="mb-0">
            <b-form-input id="ttl" name="end-ttl" placeholder="1000">

            </b-form-input>
          </b-form-group>
        </b-col>


        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Data"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="date"
            class="mb-0">
            <b-form-input id="date" name="date" placeholder="25-05">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Horas"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="hour"
            class="mb-0">
            <b-form-input id="hour" name="hour" placeholder="00">

            </b-form-input>
          </b-form-group>
        </b-col>


        <b-col lg="12" class="my-1 ">
          <b-form-group
            label="Limite"
            label-cols-sm="6"
            label-align-sm="right"
            label-size="sm"
            label-for="limit"
            class="mb-0">
            <b-form-input id="limit" name="limit" placeholder="500">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-button type="submit" variant="primary" class="buttonSearch col-lg-4 offset-lg-4 mt-3" size="md">Search <i class="fas fa-search"></i></b-button>

      </b-form>
    </div>

    <div class="screenMain">
        <a v-on:click="openTab()" href="#" class="openTab">
        <i class="fas fa-search"></i>
        </a>
        <div class="tableMain p-md-5 p-3">  
          <b-table
          stacked="xl"
          :sticky-header="stickyHeader"
          :no-border-collapse="noCollapse"
          responsive
          :items="items"
          :fields="fields"
          :current-page="currentPage"
          :per-page="perPage"
          @filtered="onFiltered"
          :filter="filter"
          :filterIncludedFields="filterOn"
          class="table table-striped"
          >
          <!-- We are using utility class `text-nowrap` to help illustrate horizontal scrolling -->
          </b-table>
        </div>

      <div class="filters">
        <div class="row mt-5">
          <b-pagination
            v-model="currentPage"
            :total-rows="totalRows"
            :per-page="perPage"
            align="fill"
            size="sm"
            class="col-md-5 offset-md-1">
          </b-pagination>
          <b-form-group
              label="Per page"
              label-cols-sm="6"
              label-cols-md="4"
              label-cols-lg="3"
              label-align-sm="right"
              label-size="sm"
              label-for="perPageSelect"
              class="mb-0 col-md-4 offset-md-1">
            <b-form-select
              v-model="perPage"
              id="perPageSelect"
              size="sm"
              :options="pageOptions">
            </b-form-select>
          </b-form-group>
        </div>  
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        totalRows: 1,
        currentPage: 1,
        perPage: 25,
        pageOptions: [25, 50, 75, 100, 250, 500],
        stickyHeader: true,
        noCollapse: false,
        filter: null,
        filterOn: [],
        fields: [
          { key: 'Source-IP', isRowHeader: true, sortable: true, label:'IP - Origem'},
          { key: 'Source-Port', isRowHeader: true, sortable: true, label:'Porta - Origem'},
          { key: 'Destination-IP', isRowHeader: true, sortable: true, label:'IP - Destino'},
          { key: 'Destination-Port', isRowHeader: true, sortable: true, label:'Porta - Destino'},
          { key: 'Protocol', isRowHeader: true, sortable: true, label: 'Protocolo'},
          { key: 'Length', isRowHeader: true,  sortable: true, label:'Comprimento'},
          { key: 'TTL', isRowHeader: true, sortable: true},


        ],
        items: []
      }
    },


    async created() {
      let response = await this.$http.get('http://localhost:5000/realtime/table')
      this.items = response.data.data.dataset
      

      this.totalRows = this.items.length
    },

    methods: {
      onFiltered(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
        this.totalRows = filteredItems.length
        this.currentPage = 1
      },
      closeTab(){
        document.querySelector('#rightBar').style.width = "0%";
        document.querySelector('#rightBar').style.display = "none";
        document.querySelector('.screenMain').style.filter = "blur(0px)"
      },
      openTab(){
        document.querySelector('#rightBar').style.width = "25%";
        document.querySelector('#rightBar').style.display = "inline";
        document.querySelector('.screenMain').style.filter = "blur(4px)"
      },
      async submit(evt){
        document.querySelector('#rightBar').style.width = "0%";
        document.querySelector('#rightBar').style.display = "none";
        document.querySelector('.screenMain').style.filter = "blur(0px)"

        
        let obj = {}
        evt.preventDefault()
        evt.target.forEach(element => {
          
          if(element.value !== '')
          
          obj[element.name] = element.value
          
        });
        
        let response = await this.$http.get('http://localhost:5000/realtime/table', {params: obj})

        this.items = response.data.data.dataset
        
        
        
      }
    },
  }
</script>

<style >

  .mainView{
    overflow-x: hidden!important;
  }


  .closeTab{
    color: #9F9F9F;
  }

  .tableMain{
    padding-bottom: 0px!important;
    margin-bottom: 0px!important;
  }

  .buttonSearch{
    font-weight: bold!important;
  }

  .openTab{
    color: #9F9F9F;
    float: right;
    margin-right:50px;
    margin-top:30px;
    font-size: 25px;
  }

  .page-link{
    background-color:#1f1f22!important;
    color: white!important;
    font-weight: bold;
  }

  select{
    background-color: #1f1f22!important;
    color: white!important;
  }

  label{
    color: white!important;
    font-weight: bold;
  }


  .closeFilter{
    font-size: 30px;
    float:left;
    margin-left: 10px;
    color: #9F9F9F;
  }

  .rightBar{
    padding-top: 10px;
    padding-right:20px; 
    width: 0%;
    display: none;
    height: 100vh;
    z-index: 9999;
    position: absolute;
    right: 0;
    background-color: #252525;
    transition: 1s;
  }

  .rightBar button{
    margin-bottom: 10px;
  }

  .rightBar label{
    color: white!important;
    font-weight: 600;
  }

  form{
    color: #335e8d;
  }

  .content{
    overflow: hidden;
  }

  .filter-2{
    background-color: #03070A;
    color: white;
  }

  table{
    background-color: #212124;
    color: white!important;
  }

  th{
    border-top: 0!important;
  }

  table > th > div{
        color: white;
  }
</style>
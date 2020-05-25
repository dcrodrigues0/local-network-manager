<template>
  <div>
      <b-form  @submit="submit" class="row">

        <b-col lg="5" class="my-1 ">
          <b-form-group
            label="IP - Origem"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="Source-IP"
            class="mb-0">
            <b-form-input id="Source-IP" name="src-ip" placeholder="185.50.107.238">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="5" class="my-1">
          <b-form-group
            label="Porta - Origem"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="Source-Port"
            class="mb-0">
            <b-form-input id="Source-Port" name="src-port" placeholder="50001">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="5" class="my-1">
          <b-form-group
            label="Min Porta - Origem"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="Start-source-port"
            class="mb-0">
            <b-form-input id="Start-source-port" name="start-src-port" placeholder="185.50.107.238">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="5" class="my-1">
          <b-form-group
            label="Max Porta - Origem"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="End-source-port"
            class="mb-0">
            <b-form-input id="End-source-port" name="end-src-port" placeholder="192.168.1.2">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="5" class="my-1">
          <b-form-group
            label="IP - Destino"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="Destination-IP"
            class="mb-0">
            <b-form-input id="Destination-IP" name="dst-ip" placeholder="192.168.1.2">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="5" class="my-1">
          <b-form-group
            label="Porta-Destino"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="Destination-Port"
            class="mb-0">
            <b-form-input id="Destination-Port" name="dst-port" placeholder="52136">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="5" class="my-1">
          <b-form-group
            label="Min Porta - Destino"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="Start-destination-Port"
            class="mb-0">
            <b-form-input id="Start-destination-Port" name="start-dst-port" placeholder="50001">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="5" class="my-1">
          <b-form-group
            label="Max Porta - Destino"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="End-destination-Port"
            class="mb-0">
            <b-form-input id="End-destination-Port" name="end-dst-port" placeholder="52136">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="3" class="my-1">
          <b-form-group
            label="Protocolo"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="Protocol"
            class="mb-0">
            <b-form-input id="Protocol" name="protocol" placeholder="UDP">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="3"  class="my-1">
          <b-form-group
            label="Min Tamanho"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="Length"
            class="mb-0">
            <b-form-input id="Length" name="start-length" placeholder="71">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="3"  class="my-1">
          <b-form-group
            label="Max Tamanho"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="Length"
            class="mb-0">
            <b-form-input id="Length" name="end-length" placeholder="922">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="3" class="my-1">
          <b-form-group
            label="Min TTL"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="ttl"
            class="mb-0">
            <b-form-input id="ttl" name="start-ttl" placeholder="58">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="3" class="my-1">
          <b-form-group
            label="Max TTL"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="ttl"
            class="mb-0">
            <b-form-input id="ttl" name="end-ttl" placeholder="64">

            </b-form-input>
          </b-form-group>
        </b-col>


        <b-col lg="3"  class="my-1">
          <b-form-group
            label="Data"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="date"
            class="mb-0">
            <b-form-input id="date" name="date" placeholder="24-05">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-col lg="3" class="my-1">
          <b-form-group
            label="Horas"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="hour"
            class="mb-0">
            <b-form-input id="hour" name="hour" placeholder="04">

            </b-form-input>
          </b-form-group>
        </b-col>


        <b-col lg="3" class="my-1">
          <b-form-group
            label="Límite"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="limit"
            class="mb-0">
            <b-form-input id="limit" name="limit" placeholder="100">

            </b-form-input>
          </b-form-group>
        </b-col>

        <b-button type="submit" variant="primary" class="col-lg-4 offset-lg-4 mt-3" size="md">Search</b-button>

      </b-form>



      <div class="row mt-5">
          <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          align="fill"
          size="sm"
          class="col-md-4 offset-md-1"
          ></b-pagination>

          <b-form-group
            label="Per page"
            label-cols-sm="6"
            label-cols-md="4"
            label-cols-lg="3"
            label-align-sm="right"
            label-size="sm"
            label-for="perPageSelect"
            class="mb-0 col-md-4 offset-md-1"
          >
            <b-form-select
              v-model="perPage"
              id="perPageSelect"
              size="sm"
              :options="pageOptions"
            ></b-form-select>
          </b-form-group>
      </div>      


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
          { key: 'Length', isRowHeader: true,  sortable: true, label:'Tamanho'},
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

      async submit(evt){
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
    background-color: #262825;
    color: white!important;
  }

  th{
    border-top: 0!important;
  }

  table > th > div{
        color: white;
  }
</style>
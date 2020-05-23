<template>
  <div>

    <b-row class="filter p-4 mb-3">

      <b-col lg="4" offset="1" class="my-1">
        <b-form-group
          label="Filter"
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          label-for="filterInput"
          class="mb-0"
        >
          <b-input-group size="sm">
            <b-form-input
              v-model="filter"
              type="search"
              id="filterInput"
              placeholder="Type to Search"
            ></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>
      </b-col>

      <b-col lg="4"  offset="1"  class="my-1">
        <b-form-group
          label="Filter On"
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          class="mb-0">
          <b-form-checkbox-group v-model="filterOn" class="mt-1">
            <b-form-checkbox value="Source_IP">Source_IP</b-form-checkbox>
            <b-form-checkbox value="Destination_IP">Destination_IP</b-form-checkbox>
            <b-form-checkbox value="Protocol">Protocol</b-form-checkbox>
            <b-form-checkbox value="Length">Length</b-form-checkbox>
            <b-form-checkbox value="TTL">TTL</b-form-checkbox>
            <b-form-checkbox value="Port">Port</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
      </b-col>

      <b-col lg="4" offset="1">
          <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          align="fill"
          size="sm"
          class="my-0"
          ></b-pagination>
      </b-col>

      <b-col lg="4" offset="1" class="my-1">
          <b-form-group
            label="Per page"
            label-cols-sm="6"
            label-cols-md="4"
            label-cols-lg="3"
            label-align-sm="right"
            label-size="sm"
            label-for="perPageSelect"
            class="mb-0"
          >
            <b-form-select
              v-model="perPage"
              id="perPageSelect"
              size="sm"
              :options="pageOptions"
            ></b-form-select>
          </b-form-group>
      </b-col>
      
    </b-row>



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
        tableData: null,
        totalRows: 1,
        currentPage: 1,
        perPage: 5,
        pageOptions: [5, 10, 15],
        stickyHeader: true,
        noCollapse: false,
        filter: null,
        filterOn: [],
        fields: [
          { key: 'Source_IP', isRowHeader: true, sortable: true},
          { key: 'Destination_IP', isRowHeader: true, sortable: true},
          { key: 'Protocol', isRowHeader: true, sortable: true},
          { key: 'Length', isRowHeader: true,  sortable: true},
          { key: 'TTL', isRowHeader: true, sortable: true},
          { key: 'Port', isRowHeader: true, sortable: true}
        ],
        items: [
          { Source_IP: 1, Destination_IP: 1, Protocol: 1, Length: 1, TTL: 1, Port: 1},
          { Source_IP: 4, Destination_IP: 4, Protocol: 4, Length: 4, TTL: 4, Port: 4},
          { Source_IP: 0, Destination_IP: 0, Protocol: 0, Length: 0, TTL: 0, Port: 0},
          { Source_IP: 1, Destination_IP: 0, Protocol: 1, Length: 2, TTL: 3, Port: 4},
          { Source_IP: 1, Destination_IP: 0, Protocol: 1, Length: 2, TTL: 3, Port: 2},
          { Source_IP: 1, Destination_IP: 0, Protocol: 1, Length: 2, TTL: 3, Port: 4},
          { Source_IP: 7, Destination_IP: 7, Protocol: 7, Length: 7, TTL: 7, Port: 7},
          { Source_IP: 1, Destination_IP: 0, Protocol: 1, Length: 2, TTL: 3, Port: 4},
          { Source_IP: 7, Destination_IP: 7, Protocol: 7, Length: 7, TTL: 7, Port: 7},
          { Source_IP: 1, Destination_IP: 0, Protocol: 1, Length: 2, TTL: 3, Port: 4},
          { Source_IP: 7, Destination_IP: 7, Protocol: 7, Length: 7, TTL: 7, Port: 7},
          { Source_IP: 1, Destination_IP: 0, Protocol: 1, Length: 2, TTL: 3, Port: 4}


        ]
      }
    },


    mounted() {
        this.$http.get('http://localhost:5000/realtime/table')
        .then(res => this.tableData = res.data)

        setInterval(() => {
          console.log(this.tableData);
          
        }, 5000);
        
      
    },


      // created(){
      //   this.$http.get('http://localhost:5000/realtime/table')
      //   .then(res => this.tableData = res.data
          
      // )},

    methods: {
        onFiltered(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
        this.totalRows = filteredItems.length
        this.currentPage = 1
      }
    },
  }
</script>

<style >

  .content{
    overflow: hidden;
  }

  .filter{
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
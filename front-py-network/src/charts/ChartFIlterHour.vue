<script>
    import { Bar } from 'vue-chartjs'

    export default {
        extends: Bar,        
        data (){
            return{
                dataChart:null
            }
        },
        props:{
          dtIni: {
            type: String,
            required: true,
          },
          hr:{
            type: String,
            required: true
          }
        },
        
        mounted(){        
          this.$http.get(`http://127.0.0.1:5000/date/hour/ipv4?date=${this.dtIni}&hour=${this.hr}&exibition=backgroundColor&subtitle=Bytes%20Trafegados`)
          .then(response => {
              this.renderChart(response.data.data, {maintainAspectRatio: false,responsive:true, scales: {
              xAxes: [{
                ticks: {
                  fontColor: "white",
                }
              }], 
              yAxes: [{
                ticks: {
                  fontColor: "white",
                }
              }]
      }});

          })
        }
    }

</script>

<style>
</style>

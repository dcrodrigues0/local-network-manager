<script>
import { HorizontalBar } from 'vue-chartjs'

export default {
  extends: HorizontalBar,
  
  data (){
    return{
      dataChart:null
    }
  },
  props:{
    dtIni: {
      type: String,
      required: true,
      default:'20-05'
    },
  },
  mounted(){
    this.$http.get(`http://localhost:5000/trafficmac?date=${this.dtIni}&exibition=backgroundColor&subtitle=QuantidadeDePacotes`)
      .then(res => this.renderChart(res.data.data,{maintainAspectRatio: false,responsive:true, scales: {
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
      }}))
      
  }
}

</script>

<style>
</style>

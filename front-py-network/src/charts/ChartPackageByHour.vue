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
      default:'23-05'
    },
  },
  mounted(){
    this.$http.get(`http://localhost:5000/date/hour?date=${this.dtIni}&exibition=backgroundColor&subtitle=Quantidade de pacotes`)
      .then(res => this.renderChart(res.data.data,
      {
        maintainAspectRatio: false,
        responsive:true,
        scales: {
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
      } 
      
      }


      ))
  }
}

</script>

<style>
</style>

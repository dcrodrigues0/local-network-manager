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
      default:'07-05'
    },
  },
  mounted(){
    this.$http.get(`http://localhost:5000/date/hour?date=${this.dtIni}`)
      .then(res => this.renderChart(res.data.data,{maintainAspectRatio: false,responsive:true}))
      
  }
}

</script>

<style>
</style>

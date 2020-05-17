<script>
import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  
  data (){
    return{
      dataChart:null
    }
  },
  created(){
    this.$http.get('http://localhost:5000/ipv4/destination?date=14-05&hour=19&exibition=backgroundColor&subtitle=Quantidade de pacotes')
    .then(res => this.renderChart(res.data.data,{maintainAspectRatio: false,responsive:true}))
      
  }
}

</script>

<style>
</style>

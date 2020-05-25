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
      default:'16-05'
    },
    dtFim: {
      type: String,
      required: true,
      default:'21'
    },
  },

  created(){
    this.$http.get(`http://localhost:5000/ipv4/destination?date=${this.dtIni}&hour=${this.dtFim}&exibition=backgroundColor&subtitle=Quantidade de pacotes`)
    .then(res => this.renderChart(res.data.data,{maintainAspectRatio: false,responsive:true}))
      
  }
}

</script>

<style>
</style>

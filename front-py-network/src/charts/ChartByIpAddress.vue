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
      default:'23-05'
    },
    dtFim: {
      type: String,
      required: true,
      default:'02'
    },
  },

  created(){
    this.$http.get(`http://localhost:5000/ipv4/source?date=${this.dtIni}&hour=${this.dtFim}&exibition=backgroundColor&subtitle=Quantidade de pacotes`)
    .then(res => this.renderChart(res.data.data,{maintainAspectRatio: false,responsive:true}))
      
  }
}

</script>

<style>
</style>

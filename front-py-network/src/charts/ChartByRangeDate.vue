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
            default:'01-05'
          },
          dtFim: {
            type: String,
            required: true,
            default:'03-05'
          },
        },
        mounted(){        
          this.$http.get(`http://localhost:5000/range?start=${this.dtIni}&end=${this.dtFim}&exibition=backgroundColor&subtitle=Quantidade De Pacotes`)
          .then(res => this.renderChart(res.data.data,{maintainAspectRatio: false,responsive:true}))
        }
    }

</script>

<style>
</style>

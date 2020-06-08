<script>
    import { Line } from 'vue-chartjs'

    export default {
        extends: Line,        
        data (){
            return{
                dataChart:null
            }
        },
        mounted(){
            setInterval(() => {
                this.$http.get('http://localhost:5000/realtime?exibition=borderColor&subtitle=Quantidade De Pacotes')
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
            }, 30000);
        }
    }

</script>

<style>
</style>

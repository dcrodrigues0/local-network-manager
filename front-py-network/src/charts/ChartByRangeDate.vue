<script>
    import { Bar } from 'vue-chartjs'

    export default {
        extends: Bar,        
        data (){
            return{
                dataChart:null
            }
        },
        mounted(){
            
            this.$http.get('http://localhost:5000/date/hour?date=07-05')
            .then(res => this.renderChart(res.data.data,{maintainAspectRatio: false,responsive:true}))
        }
    }

</script>

<style>
</style>

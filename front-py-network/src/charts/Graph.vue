<script>
    import { Line } from 'vue-chartjs'
    import axios from 'axios';
    export default {
        extends: Line,
        mounted () {
            axios
            .get('https://api.npoint.io/4f39c15ab9ef59fb624e')
            .then(response => (this.renderChart(response.data, {
                    maintainAspectRatio: false, 
                    responsive: true, 
                    scales: {
                        xAxes: [{
                        ticks: {
                            fontColor: 'rgba(81, 83, 69, 1)',
                            fontSize: 15
                        }
                        }],
                        yAxes: [{
                        ticks: {
                            fontColor: 'rgba(81, 83, 69, 1)',
                            fontSize: 12
                        }
                        }]
                    
                    }

                }
            )))
        },
        data () {
            return {
                chartdata:null,
            }
        },
    }
</script>

<style>
</style>

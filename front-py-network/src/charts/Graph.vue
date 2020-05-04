<script>
    import { Line } from 'vue-chartjs'
    import axios from 'axios';
    export default {
        extends: Line,
        mounted () {
            axios
            .get('https://api.npoint.io/4f39c15ab9ef59fb624e')
            .then(response => (this.renderChart(response.data, {responsive: true, maintainAspectRatio:false})))
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

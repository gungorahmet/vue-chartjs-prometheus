<!-- Based on https://vue-chartjs.org/guide/#chart-with-local-data -->

<template>
  <div class="container">
    <Line v-if="loaded"
        :data="chartData"
        :options="chartOptions"
        :width="1250"
        :height="500"
    />
    <span v-if="!loaded"> Waiting for the chart.. </span>
  </div>
</template>

<script lang="ts">
import { Line } from 'vue-chartjs'
import 'chart.js/auto'

export default {
  name: 'LineChart',
  components: { Line },
  data: () => ({
    loaded: false,
    chartData: {
            "labels": [],
            "datasets": []
        },
    chartOptions: {},
  }),
  async mounted () {
    this.loaded = false

    try {
      const response = await fetch('http://localhost:8000/api/v1/get_dumb_data')
      const responseJSON = await response.json()

      this.chartData = responseJSON.chart.chartData;
      this.chartOptions = responseJSON.chart.chartOptions;
      this.loaded = true;
    } catch (e) {
      console.error(e)
    }
  }
}
</script>

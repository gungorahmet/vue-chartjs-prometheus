<!-- Based on https://vue-chartjs.org/guide/#chart-with-local-data -->

<template>

  <div class="container">
    <div>
      <select v-model="selectedItem" @change="fetchData">
        <option v-for="item in dropdownItems" :value="item" :key="item.id">{{ item.name }}</option>
      </select>
    </div>

    <Doughnut v-if="loaded"
          :data="chartData"
          :options="chartOptions"
    />
    <span v-if="!loaded"> Waiting for the chart.. </span>
  </div>
</template>

<script lang="ts">
import { Doughnut } from 'vue-chartjs'
import 'chart.js/auto'
import axios from 'axios';

export default {
  name: 'DoughnutChart',
  components: { Doughnut },
  data: () => ({
    loaded: false,
    chartData: {
            "labels": [],
            "datasets": []
        },
    chartOptions: {},
    selectedItem: {
              id: 4
            },
    dropdownItems: [
      { id: 1, name: 'Option 1' },
      { id: 2, name: 'Option 2' },
      { id: 3, name: 'Option 3' },
      { id: 4, name: 'Option 4' },
    ],
  }),

  async mounted () {
    this.loaded = false
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/get_dumb_doughnut_chart_data', {
          params: {
            option: this.selectedItem.id
          }
        });
        const data = response.data;
        console.log(this.selectedItem.id);
        console.log(data);

        this.chartData = data.chart.chartData;
        this.chartOptions = data.chart.chartOptions;
        this.loaded = true;
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>

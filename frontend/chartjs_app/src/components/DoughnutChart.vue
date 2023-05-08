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

<script>
import { Doughnut } from 'vue-chartjs'
import 'chart.js/auto'
import axios from 'axios';

import { Chart, registerables } from 'chart.js'

var percentage = "12.34%"

const plugin = {
    id: 'custom_canvas_background_color',
    afterDraw: (chart, args, options) => {
      if (chart.config.type === 'doughnut') {  // Here need to be fixed to register specific chart.
        const {ctx} = chart;
        ctx.save();
        // ctx.fillRect(0, 0, chart.width, chart.height);

        // const x = chart.getDatasetMeta(0).data[0].x;
        // const y = chart.getDatasetMeta(0).data[0].y;

        ctx.font = 'bold 50px sans-serif';
        // ctx.fillText("99.87%", 115, 180);
        // ctx.fillText("99.87%", 145, 240);
        ctx.fillText(percentage, 145, 240);
        // console.log(chart.width, chart.height);
        
        // ctx.restore();
      }
    }
}

// Chart.register(...registerables, plugin)

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
    Chart.register(plugin);
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

        // if (this.selectedItem.id === 1) {
        //     percentage = data.chart.chartData.datasets.data[0] + "%"
        // }
        // else if (this.selectedItem.id === 2) {
        //     percentage = "85.90%"
        // }
        // else if (this.selectedItem.id === 3) {
        //     percentage = "30.48%"
        // }
        // else {
        //     percentage = "12.34%"
        // }
        console.log("HERE");
        console.log(data.chart.chartData.datasets[0].data[0]);
        percentage = data.chart.chartData.datasets[0].data[0] + "%";
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

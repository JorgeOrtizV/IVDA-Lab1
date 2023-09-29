<template>
      <div>
        <v-row align="center" justify="center" class="mt-1 mb-0">
          <h3>Employment Comparison: {{ $props.selectedCompany }}</h3>
        </v-row>
        <div style="height: 90vh">
          <div id='myBarPlot' style="height: inherit"></div>
        </div>
      </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: 'BarPlot',
  props: ["selectedCompany", "companyIdx", "selectedCategory"],
  data: () => ({
    BarPlotData: {company: [], companies: []}
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      // req URL to retrieve single company from backend
      var reqUrl = 'http://127.0.0.1:5000/companies/' + this.$props.companyIdx + '?algorithm=none'
      console.log("ReqURL BarPlot " + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();
      // transform data to usable by Barplot
      this.BarPlotData.company.push(responseData.employees)
      console.log(this.BarPlotData.company)

      var reqUrl_2 = 'http://127.0.0.1:5000/companies?category=' + this.$props.selectedCategory
      console.log("ReqURL " + reqUrl_2)
      // await response and data
      const response_2 = await fetch(reqUrl_2)
      const responseData_2 = await response_2.json();
      // transform data to usable by barplot
      responseData_2.forEach((company) => {
        this.BarPlotData.companies.push(company.employees)
      })
      // draw the Barplot after the data is transformed
      this.drawBarPlot()
    },
    
    drawBarPlot() {
      var sum = this.BarPlotData.companies.reduce((partialSum, a) => partialSum + a, 0);
      var average = sum/this.BarPlotData.companies.length;
      
      var trace1 = {
        x: [this.$props.selectedCompany, 'Average', 'Total'],
        y: [this.BarPlotData.company[0], average, sum],
        marker:{
            color:['orange', 'green', 'blue']
        },
        type: 'bar',
      };

      var data = [trace1];
      var layout = {
        xaxis: {
          title: '<b>Company, average, and total comparison</b>',
          font: {
            family: 'Courier New, monospace',
            size: 24,
            color: '#000000'
          }
        },
        yaxis: {
          title: '<b>Number of employees</b>',
          font: {
            family: 'Courier New, monospace',
            size: 24,
            color: '#000000'
          }
        }
      }
      var config = {responsive: true, displayModeBar: false}
      
      Plotly.newPlot('myBarPlot', data, layout, config);
    }
  },
  watch: {
    selectedCompany() {
    this.BarPlotData.x = [];
    this.BarPlotData.company = [];
    this.BarPlotData.companies = [];

    this.fetchData();
    },
    selectedCategory: function () {
    this.BarPlotData.company = [];
    this.BarPlotData.companies = [];

        this.fetchData();
    }
  },
}
</script>
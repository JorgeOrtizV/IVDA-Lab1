<template>
  <div>
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="2" class="sideBar">
          <v-card class="background_panel">
            <v-row>
              <v-col cols="12" sm="12">
                <div class="control-panel-font">&nbspCompany Overview</div>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="10" sm="12">
                  <v-select class="select_box"
                      :items="categories.values"
                      label="Select a category"
                      dense
                      v-model="categories.selectedValue"
                      @change="changeCategory"
                  ></v-select>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" sm="12">
                  <div class="control-panel-font">&nbspProfit View of Company</div>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" sm="12">
                  <v-select class="select_box"
                      :items="companies.values"
                      label="Select a company"
                      dense
                      v-model="companies.selectedValue"
                      @change="changeCompany"
                  ></v-select>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" sm="12">
                  <v-select class="select_box"
                      :items="algorithm.values"
                      label="Select an algorithm"
                      dense
                      v-model="algorithm.selectedValue"
                      @change="changeAlgorithm"
                  ></v-select>
              </v-col>
            </v-row>

          </v-card>
        </v-col>
        <v-col cols="12" md="5">
          <ScatterPlot :key="scatterPlotId" :selectedCategory="categories.selectedValue" @changeCurrentlySelectedCompany="changeCurrentlySelectedCompany"/>
        </v-col>
        <v-col cols="12" md="5">
          <LinePlot :key="linePlotId"
            :selectedCompany="companies.selectedValue"
            :companyIdx="this.companies.values.indexOf(this.companies.selectedValue)+1"
            :selectedAlgorithm="algorithm.selectedValue"/>
        </v-col>
        <v-col cols="12" md="5">
          <BarPlot :key="barPlotId" :selectedCategory="categories.selectedValue" 
                    :selectedCompany="companies.selectedValue"
                    :companyIdx="this.companies.values.indexOf(this.companies.selectedValue)+1"/>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import ScatterPlot from './ScatterPlot';
import LinePlot from './LinePlot';
import BarPlot from './BarPlot';
export default {
  components: {ScatterPlot, LinePlot, BarPlot},
  data: () => ({
    categories: {
      values: ['All', 'tech', 'health', 'bank'],
      selectedValue: 'All'
    },
    companies: {
      values: ['alphabet', 'apple', 'amazon','microsoft','meta','united health', 'johnson and johnson','pfizer','cvs health', 'mckesson','ubs','credit suisse', 'jp morgan', 'goldman sachs', 'bank of america'],
      selectedValue: 'alphabet',
      companyIdx: 1
      //companyIdx : this.values.indexOf(this.selectedValue)
    },
    algorithm: {
      values: ['none', 'random', 'regression'],
      selectedValue: 'none'
    }
  }),

  methods: {
  changeCategory() {
        this.scatterPlotId += 1
      },

  changeCompany() {
        this.linePlotId += 1
      },
  changeAlgorithm() {
        this.linePlotId += 1
      },
  changeCurrentlySelectedCompany(companyId) {
        this.companies.selectedValue = this.companies.values[companyId-1]
        this.changeCompany()
      },
  
  }
}
</script>

<style scoped>
.control-panel-font {
  font-family: "Open Sans", verdana, arial, sans-serif;
  font-weight: bold;
  align-items: center;
  font-size: 18px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  display: flex;
  font-weight: 500;
  height: 50px;
  background-color:  #ceeffa;
}
.sideBar {
  border-right: 1px solid rgba(0, 0, 0, 0.1);
  background: #fafafa;
  padding-left: 17px;
  height: calc(100vh - 50px);
  background-color: #a9c4f8; 
}
</style>



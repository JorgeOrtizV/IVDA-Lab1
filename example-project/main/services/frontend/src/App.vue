<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <h2>Jorge Alejandro Ortiz Valerio, 23-743-958</h2>
    </v-app-bar>
    <v-main>
      <ConfigurationPanel/>
    </v-main>
  </v-app>
</template>

<style>
/* disable scrolling */
html {
  scrollbar-width: none; /* For Firefox */
  -ms-overflow-style: none; /* For Internet Explorer and Edge */
}
html::-webkit-scrollbar {
  width: 0px; /* For Chrome, Safari, and Opera */
}
</style>


<script>
import ConfigurationPanel from './components/ConfigurationPanel.vue'

export default {
  name: 'App',

  components: {
    ConfigurationPanel,
  },

  data: () => ({
    scatterPlotId: 0,
    linePlotId: 0,
    barPlotId: 0
  }),

}
</script>

<template>
  <div>
    <Top></Top>
    <AgeScreenTime/>
    <ScreenTimeVsHappiness />
  </div>
</template>

<script>
// @ is an alias to /src
import { mapActions } from "vuex";

import Top from '@/components/data/Top.vue'
import AgeScreenTime from '@/components/graphs/AgeScreenTime.vue'
import ScreenTimeVsHappiness from '@/components/graphs/ScreenTimeVsHappiness.vue'

export default {
  name: 'DataView',
  components: {
    Top, 
    AgeScreenTime, 
    ScreenTimeVsHappiness,
  },
  mounted() {
    this.getDataForGraphs();
  },
  methods: {
    ...mapActions("datapage", ["grabGraphData"]),
    getDataForGraphs() {
      this.grabGraphData()
    }, 
  }, 
}

</script>

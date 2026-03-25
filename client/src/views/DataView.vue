<template>
  <div>
    <Top></Top>
    <AgeScreenTime/>
    <ScreenTimeVsHappiness />
    <SleepVsStress />
    <DetoxVsHappiness />
  </div>
</template>

<script>
// @ is an alias to /src
import { mapActions } from "vuex";

import Top from '@/components/data/Top.vue'
import AgeScreenTime from '@/components/graphs/AgeScreenTime.vue'
import ScreenTimeVsHappiness from '@/components/graphs/ScreenTimeVsHappiness.vue'
import SleepVsStress from '@/components/graphs/SleepVsStress.vue'
import DetoxVsHappiness from '@/components/graphs/DetoxVsHappiness.vue'

export default {
  name: 'DataView',
  components: {
    Top, 
    AgeScreenTime, 
    ScreenTimeVsHappiness,
    SleepVsStress,
    DetoxVsHappiness,
  },
  async created() {
    await this.getDataForGraphs();
    this.loading = false;
  },
  methods: {
    ...mapActions("datapage", ["grabGraphData"]),
    getDataForGraphs() {
      this.grabGraphData()
    }, 
  }, 
}

</script>

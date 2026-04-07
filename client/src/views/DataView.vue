<template>
  <div>
    <Top></Top>
    <AgeScreenTime/>
    <ScreenTimeVsHappiness />
    <SleepVsStress />
    <DetoxVsStress />
    <ExerciseVsHappiness />
  </div>
</template>

<script>
// @ is an alias to /src
import { mapActions } from "vuex";

import Top from '@/components/data/Top.vue'
import AgeScreenTime from '@/components/graphs/AgeScreenTime.vue'
import ScreenTimeVsHappiness from '@/components/graphs/ScreenTimeVsHappiness.vue'
import SleepVsStress from '@/components/graphs/SleepVsStress.vue'
import DetoxVsStress from '@/components/graphs/DetoxVsStress.vue'
import ExerciseVsHappiness from '@/components/graphs/ExerciseVsHappiness.vue'

export default {
  name: 'DataView',
  components: {
    Top, 
    AgeScreenTime, 
    ScreenTimeVsHappiness,
    SleepVsStress,
    DetoxVsStress,
    ExerciseVsHappiness,
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

<template>
  <div>
    <Top></Top>
    <div class="graph-div">
    <AgeScreenTime/>
    <ScreenTimeVsHappiness />
    <SleepVsStress />
    <DetoxVsStress />
    <ExerciseVsHappiness />
    <SocialMediaGraph />
    <SocialMediaHoursGraph />
    </div>
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
import SocialMediaGraph from '@/components/graphs/SocialMediaPlatform.vue'
import SocialMediaHoursGraph from '@/components/graphs/SocialMediaHoursGraph.vue'

export default {
  name: 'DataView',
  components: {
    Top, 
    AgeScreenTime, 
    ScreenTimeVsHappiness,
    SleepVsStress,
    DetoxVsStress,
    ExerciseVsHappiness,
    SocialMediaGraph,
    SocialMediaHoursGraph,
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

<style scoped>

.graph-div {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  margin: 2%;
}

</style>

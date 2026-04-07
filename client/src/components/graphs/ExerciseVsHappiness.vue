<template>
  <div>
    booh
    <div ref="ExerciseVsHappinessGraph"></div>
  </div>
</template>


<script>
import * as d3 from "d3";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ExerciseVsSleep",
  computed: {
    ...mapGetters("datapage", ["sleepvsstressData"]),
  },

}

</script>
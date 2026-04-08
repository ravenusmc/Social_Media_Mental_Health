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
    ...mapGetters("datapage", ["ExerciseVsHappiness"]),
  },
  mounted() {
    this.buildExerciseVsHappinessGraph();
  },
  methods: {
    buildExerciseVsHappinessGraph() {

      // Remove old SVG
      d3.select(this.$refs.ExerciseVsHappinessGraph).selectAll("*").remove();

      const margin = { top: 50, right: 30, bottom: 50, left: 70 };
      const width = 460 - margin.left - margin.right;
      const height = 400 - margin.top - margin.bottom;

      const svg = d3
        .select(this.$refs.ExerciseVsHappinessGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    }
  }

}

</script>
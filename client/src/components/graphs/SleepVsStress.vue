<template>
  <div>
    <div ref="SleepVsStressGraph"></div>
  </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "SleepVsStress",
  computed: {
    ...mapGetters("datapage", ["sleepvsstressData"]),
  },
  mounted() {
    this.buildSleepVsStressGraph();
  },
  methods: {
    buildSleepVsStressGraph() {

      // Remove old SVG
      d3.select(this.$refs.SleepVsStressGraph).selectAll("*").remove();

      const margin = { top: 50, right: 30, bottom: 50, left: 70 };
      const width = 460 - margin.left - margin.right;
      const height = 400 - margin.top - margin.bottom;

      const svg = d3
        .select(this.$refs.SleepVsStressGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);
      
      // X axis
      const x = d3
        .scaleBand()
        .range([0, width])
        .domain(this.sleepvsstressData.map((d) => d[0]))
        .padding(0.2);
      svg.append("g").attr("transform", `translate(0,${height})`).call(d3.axisBottom(x));
    }
  }
}

</script>
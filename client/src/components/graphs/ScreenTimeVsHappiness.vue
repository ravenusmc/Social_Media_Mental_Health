<template>
  <div>
    <div ref="AgeScreenHappinessGraph"></div>
  </div>
</template>

<script> 
import * as d3 from "d3";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "AgeScreenTime",
  computed: {
    ...mapGetters("datapage", ["ScreenTimeVsHappiness"]),
  },
  watch: {
    ScreenTimeVsHappiness: {
      handler: "buildTimeVsHappinessGraph",
      deep: true,
    },
  },
  mounted() {
    this.buildTimeVsHappinessGraph();
  },
  beforeDestroy() {
    // Remove SVG and tooltips when leaving page
    d3.select(this.$refs.AgeScreenHappinessGraph).selectAll("*").remove();

    // Hide popup if still open
    const popup = document.getElementById("popup");
    if (popup) popup.style.display = "none";
  },
  methods: {
    buildTimeVsHappinessGraph() {

      // Remove old SVG
      d3.select(this.$refs.AgeScreenHappinessGraph).selectAll("*").remove();

      const margin = { top: 50, right: 30, bottom: 50, left: 70 };
      const width = 460 - margin.left - margin.right;
      const height = 400 - margin.top - margin.bottom;

      const svg = d3
        .select(this.$refs.AgeScreenHappinessGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);
      
      // X axis (Screen Time)
      const x = d3.scaleLinear()
        .domain([
          d3.min(this.ScreenTimeVsHappiness, d => d[0]),
          d3.max(this.ScreenTimeVsHappiness, d => d[0])
        ])
        .range([0, width]);
      
      svg.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x));

      // Y axis (Happiness)
      const y = d3.scaleLinear()
        .domain([
          0,
          d3.max(this.ScreenTimeVsHappiness, d => d[1])
        ])
        .range([height, 0]);

      svg.append("g")
        .call(d3.axisLeft(y));

      // Add dots
      svg.append("g")
        .selectAll("circle")
        .data(this.ScreenTimeVsHappiness)
        .enter()
        .append("circle")
        .attr("cx", d => x(d[0]))
        .attr("cy", d => y(d[1]))
        .attr("r", 4);
      
      svg
        .append("text")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 10)
        .attr("text-anchor", "middle")
        .attr("font-weight", "bold")
        .text("Screen Time (Hours)");
      
      // Y-Axis Label 
      svg
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("x", -height / 2)
        .attr("y", -margin.left + 20)
        .attr("text-anchor", "middle")
        .attr("font-weight", "bold")
        .text("Happiness (1-10)");
      
      // Title 
      svg
        .append("text")
        .attr("x", width / 2)
        .attr("y", -margin.top / 2 + 10)
        .attr("text-anchor", "middle")
        .attr("font-weight", "bold")
        .text("Screen Time Vs Happiness (Graph 2)");

    }
  }, 
}

</script>
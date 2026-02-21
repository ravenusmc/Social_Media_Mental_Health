<template>
  <div>
    Graph
    <div ref="AgeScreenTimeGraph"></div>

    <!-- Popup -->
    <!-- <div id="popup">
      <div id="popupContent" class="popup-scroll"></div>
      <button @click="closePopup">Close</button>
    </div> -->
  </div>
</template>

<script> 
import * as d3 from "d3";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "AgeScreenTime",
  computed: {
    ...mapGetters("datapage", ["AgeVsScreenTimeData"]),
  },
  mounted() {
    this.buildAgeScreenTimeGraph();
  },
  beforeDestroy() {
    // Remove SVG and tooltips when leaving page
    d3.select(this.$refs.AgeScreenTimeGraph).selectAll("*").remove();

    // Hide popup if still open
    const popup = document.getElementById("popup");
    if (popup) popup.style.display = "none";
  },
  methods: {
    buildAgeScreenTimeGraph() {

      // Remove old SVG
      d3.select(this.$refs.AgeScreenTimeGraph).selectAll("*").remove();

      const margin = { top: 50, right: 30, bottom: 50, left: 70 };
      const width = 460 - margin.left - margin.right;
      const height = 400 - margin.top - margin.bottom;

      const svg = d3
        .select(this.$refs.AgeScreenTimeGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);
      
      // X axis
      const x = d3
        .scaleBand()
        .range([0, width])
        .domain(this.AgeVsScreenTimeData.map((d) => d[0]))
        .padding(0.2);
      svg.append("g").attr("transform", `translate(0,${height})`).call(d3.axisBottom(x));

      // Y axis
      const y = d3
        .scaleLinear()
        .domain([0, d3.max(this.AgeVsScreenTimeData, (d) => d[1])])
        .range([height, 0]);
      svg.append("g").call(d3.axisLeft(y));

      // Bars
      svg
        .selectAll("rect")
        .data(this.AgeVsScreenTimeData)
        .enter()
        .append("rect")
        .attr("x", (d) => x(d[0]))
        .attr("y", height)
        .attr("width", x.bandwidth())
        .attr("height", 0)
        .attr("fill", "#121212")
        .on("click", (event, d) => this.handleBarClick(d, event))
        // .on("mouseover", showTooltip)
        // .on("mousemove", moveTooltip)
        // .on("mouseleave", hideTooltip)
        .transition()
        .duration(1500)
        .attr("y", (d) => y(d[1]))
        .attr("height", (d) => height - y(d[1]));

    }
  },
}

</script>

<style scoped></style>
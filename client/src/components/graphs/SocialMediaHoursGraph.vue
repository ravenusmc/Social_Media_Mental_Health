<template>
  <div>
    <div ref="SocialMediaHoursGraph"></div>
    test
  </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "SocialMediaHoursGraph",
  computed: {
    ...mapGetters("datapage", ["socialMediaHours"]),
  },
  mounted() {
    this.buildSocialMediaHoursGraph();
  },
  methods: {
    buildSocialMediaHoursGraph(){
      
      // Remove old SVG
      d3.select(this.$refs.SocialMediaHoursGraph).selectAll("*").remove();

      const margin = { top: 50, right: 30, bottom: 50, left: 70 };
      const width = 460 - margin.left - margin.right;
      const height = 400 - margin.top - margin.bottom;

      const svg = d3
        .select(this.$refs.socialMediaHours)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);
    },
  },
}

</script>

<stlye scoped>


</stlye>
<template>
  <div>
    tst
    <div ref="AgeScreenHappinessGraph"></div>
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
    d3.select(this.$refs.AgeScreenHappinessGraph).selectAll("*").remove();

    // Hide popup if still open
    const popup = document.getElementById("popup");
    if (popup) popup.style.display = "none";
  },
  methods: {
  }, 
}

</script>
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
    },
  },
}

</script>

<stlye scoped>


</stlye>
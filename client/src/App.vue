<template>
  <div>
    <NavBar />
    <router-view/>
    <Footer />
  </div>
</template>

<script>
import NavBar from "./components/common/NavBar.vue";
import Footer from "@/components/common/Footer.vue";

export default {
  name: 'App',
  components: {
    NavBar,
    Footer,
  }
}
</script>

<style>

</style>

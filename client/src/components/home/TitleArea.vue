<template>
  <div>
    <div class="jumbotron">
      <div class="title-box">
        <h1>Social Media and Mental Health</h1>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "TitleArea",
}
</script>

<style scoped>

.jumbotron {
  width: 100%;
  height: 650px;
  border-radius: 10px;
  background: url("../../assets/images/girl.jpg") center/cover no-repeat;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
  display: flex; 
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

</style>
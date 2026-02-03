<template>
  <div>
    <div class="main-div">
      <div>
        <h2>Purpose</h2>
        <p class="into-paragraph">
          This is another one of my projects that I choose by seeing an interesting data set on Kaggle. The project 
          is on social media health. There seems to be an article everywhere these days on social media health and we 
          all know it ain't good. The Anxious Generation, by Jonathan Haidt, really nails this. I deciided to do the project 
          simply as a good way to look at a decent, small dataset. We will see where it goes! 
        </p>
      </div>
      <div class="picture-div">

      </div>
    </div>
  </div>
</template>

<script>


</script>

<style scoped>

.main-div {
  border: 2px solid red; 
  display: grid; 
  grid-template-columns: 1fr 1fr;
  margin: 5%;
}

h2 {
  text-align: center;
  text-transform: uppercase;
}

.into-paragraph {
  font-size: 25px;
}

.picture-div {
  width: 100%;
  height: 650px;
  border-radius: 10px;
  background: url("../../assets/images/div_landing_photo.jpg") center/cover no-repeat;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
  display: flex; 
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

</style>
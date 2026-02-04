<template>
  <div>
    <div class="main-div">
      <div class="paragraph-div">
        <h2>Purpose</h2>
        <p class="into-paragraph">
          This is another project I chose after coming across an interesting dataset on Kaggle, this time focused on social media 
          and mental health. It feels like there is an article or study everywhere these days warning about the psychological costs 
          of constant connectivity, comparison, and online validation—and most of us instinctively know that the overall impact has 
          not been great. Jonathan Haidt’s The Anxious Generation captures this problem especially well, tracing how digital life has 
          reshaped childhood, adolescence, and even adulthood in ways we are only beginning to understand.
        </p>
        <p class="into-paragraph">
          I decided to take on this project partly as a way to work with a manageable, well-structured dataset, but also as an 
          opportunity to engage more seriously with these questions. Data analysis can sometimes feel abstract, but behind every 
          number is a real human experience. My hope is that this project will help reveal patterns that go beyond anecdotes and 
          headlines, offering a clearer picture of how social media intersects with mental health. For now, this is an exploratory 
          effort—one that may grow in unexpected directions as the analysis unfolds.
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
  display: grid; 
  grid-template-columns: 1fr 1fr;
  margin: 8%;
}

.paragraph-div {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
  padding: 5%;
  border-radius: 15px;
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
  height: 750px;
  border-radius: 10px;
  background: url("../../assets/images/div_landing_photo.jpg") center/cover no-repeat;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
  display: flex; 
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-left: 5%;
}

</style>
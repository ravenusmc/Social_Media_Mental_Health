import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const data = {

  AgeVsScreenTimeData: [
	['10-19', 5.5], 
	['20-29', 5.46], 
	['30-39', 5.58], 
	['40-49', 5.55], 
	['50-59', 0.0], 
	['60-69', 0.0], 
	['70-79', 0.0], 
	['80-89', 0.0]
],
  ScreenTimeVsHappiness: [],
  sleepvsstressData: [],
  detoxDaysVsStress: [],
  ExerciseVsHappiness: [],
  socialMediaData: [
    ['TikTok', 95], 
    ['X (Twitter)', 88], 
    ['LinkedIn', 87], 
    ['Facebook', 81], 
    ['YouTube', 75], 
    ['Instagram', 74]
  ],
  socialMediaHours: [
    ['Facebook', 458.3], 
    ['LinkedIn', 460.4], 
    ['YouTube', 410.90000000000003], 
    ['TikTok', 518.5], 
    ['X (Twitter)', 467.0], 
    ['Instagram', 449.9]
  ], 
}

const getters = {
  AgeVsScreenTimeData: (state) => state.AgeVsScreenTimeData,
  ScreenTimeVsHappiness: (state) => state.ScreenTimeVsHappiness,
  sleepvsstressData: (state) => state.sleepvsstressData, 
  detoxDaysVsStress: (state) => state.detoxDaysVsStress,
  ExerciseVsHappiness: (state) => state.ExerciseVsHappiness, 
  socialMediaData: (state) => state.socialMediaData, 
  socialMediaHours: (state) => state.socialMediaHours, 
};

const actions = {

  grabGraphData: ({ commit }) => {
		const path = 'http://localhost:5000/getInitialDataForGraphs';
		axios.get(path)
			.then((res) => {
        // console.log(res.data)
				commit('setScreenTimeVsHappiness', res.data['Screen_vs_Happeniness'])
        commit('setSleepVsStressData', res.data['sleep_vs_stress'])
        commit('setDetoxDaysVsStress', res.data['detox_days_vs_stress'])
        commit('setExerciseVsHappiness', res.data['exercise_vs_happiness'])
			})
			.catch((error) => {
				console.log(error);
			});
	},


};

const mutations = {

  setScreenTimeVsHappiness(state, value) {
		state.ScreenTimeVsHappiness = value;
	},

  setSleepVsStressData(state, value) {
    state.sleepvsstressData = value; 
  },

  setDetoxDaysVsStress(state, value) {
    state.detoxDaysVsStress = value
  },

  setExerciseVsHappiness(state,value) {
    state.ExerciseVsHappiness = value 
  }
};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};
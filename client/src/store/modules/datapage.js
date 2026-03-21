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
  detoxDaysVsHappiness: [],

}

const getters = {
	AgeVsScreenTimeData: (state) => state.AgeVsScreenTimeData,
  ScreenTimeVsHappiness: (state) => state.ScreenTimeVsHappiness,
  sleepvsstressData: (state) => state.sleepvsstressData, 
  detoxDaysVsHappiness: (state) => state.detoxDaysVsHappiness

};

const actions = {

  grabGraphData: ({ commit }) => {
		const path = 'http://localhost:5000/getInitialDataForGraphs';
		axios.get(path)
			.then((res) => {
        console.log(res.data)
				commit('setScreenTimeVsHappiness', res.data['Screen_vs_Happeniness'])
        commit('setSleepVsStressData', res.data['sleep_vs_stress'])
        commit('setDetoxDaysVsHappiness', res.data['detox_days_vs_happiness'])
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

  setDetoxDaysVsHappiness(state, value) {
    state.detoxDaysVsHappiness = value
  }
};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};
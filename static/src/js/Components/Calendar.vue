<template>
  <div class="grid grid-cols-7 gap-1 max-w-md mr-auto items-center">
    <button @click="previousMonth" class="bg-gray-200 p-1 rounded col-start-1 text-sm">Previous</button>
    <span class="col-span-5 text-center mb-8">{{ currentYear }} - {{ currentMonth + 1 }}</span>
    <button @click="nextMonth" class="bg-gray-200 p-1 rounded col-start-7 text-sm">Next</button>
    <div v-for="n in firstDayOfMonth" :key="'empty-' + n" class="p-2"></div>
    <div v-for="day in days" :key="day" class="p-2 border rounded text-center">
      {{ day }}
      <div class="flex justify-center mt-1">
        <span v-for="n in events[`${currentYear}-${currentMonth + 1}-${day}`] || 0" :key="n"
          class="w-1 h-1 bg-blue-500 rounded-full mx-0.5"></span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const currentMonth = ref(new Date().getMonth());
const currentYear = ref(new Date().getFullYear());

const daysInMonth = (month, year) => new Date(year, month + 1, 0).getDate();

const firstDayOfMonth = computed(() => new Date(currentYear.value, currentMonth.value, 1).getDay());

const days = computed(() => {
  const daysArray = [];
  const totalDays = daysInMonth(currentMonth.value, currentYear.value);
  for (let i = 1; i <= totalDays; i++) {
    daysArray.push(i);
  }
  return daysArray;
});

const events = ref({
  // Example events
  '2025-2-15': 2,
  '2025-2-20': 1,
});

function previousMonth() {
  if (currentMonth.value === 0) {
    currentMonth.value = 11;
    currentYear.value -= 1;
  } else {
    currentMonth.value -= 1;
  }
}

function nextMonth() {
  if (currentMonth.value === 11) {
    currentMonth.value = 0;
    currentYear.value += 1;
  } else {
    currentMonth.value += 1;
  }
}
</script>

<template>
  <div class="register-page">
    <!-- Subtle Mathematical Curves Background -->
    <div class="math-curves-bg" aria-hidden="true">
      <svg class="math-curves-svg animated-wave-1" viewBox="0 0 1440 900" fill="none">
        <path d="M-100 450 C 300 200, 600 700, 1000 350 C 1250 150, 1400 500, 1600 400" stroke="rgba(229, 178, 46, 0.08)" stroke-width="1.5" />
        <path d="M-50 550 C 350 300, 700 800, 1100 450" stroke="rgba(147, 197, 253, 0.05)" stroke-width="1" />
      </svg>
    </div>

    <div class="container register-container">
      <div class="editorial-card-wrapper">
        <router-link to="/" class="back-link">
          <span class="arrow">←</span> Bosh sahifaga qaytish
        </router-link>

        <div class="form-header">
          <h1 class="form-title">
            Olimpiadaga <span class="serif-italic-gold">ro'yxatdan</span> <span class="serif-italic">o'tish</span>
          </h1>
          <p class="form-desc">
            Viloyat matematika olimpiadasida qatnashish uchun ma'lumotlaringizni kiriting.
          </p>
        </div>

        <div v-if="serverError" class="error-banner" role="alert">
          {{ serverError }}
        </div>

        <form @submit.prevent="handleSubmit" novalidate class="register-form">
          <!-- Full Name -->
          <div class="form-group" :class="{ error: errors.full_name }">
            <label for="full_name" class="form-label">
              <span>F.I.SH. (O'QUVCHINING TO'LIQ ISMI)</span>
              <span class="required-star">*</span>
            </label>
            <input
              id="full_name"
              v-model="form.full_name"
              type="text"
              class="form-input"
              placeholder="Masalan: Karimov Jasurbek Alisher o'g'li"
              autocomplete="name"
              required
              @blur="validateField('full_name')"
            />
            <span v-if="errors.full_name" class="field-error">{{ errors.full_name }}</span>
          </div>

          <!-- Phone & Class Row -->
          <div class="form-row">
            <div class="form-group" :class="{ error: errors.phone }">
              <label for="phone" class="form-label">
                <span>TELEFON RAQAMI</span>
                <span class="required-star">*</span>
              </label>
              <input
                id="phone"
                v-model="form.phone"
                type="tel"
                class="form-input font-mono"
                placeholder="+998 90 123 45 67"
                autocomplete="tel"
                required
                @blur="validateField('phone')"
                @input="formatPhone"
              />
              <span v-if="errors.phone" class="field-error">{{ errors.phone }}</span>
            </div>

            <div class="form-group" :class="{ error: errors.class_number }">
              <label for="class_number" class="form-label">
                <span>SINF</span>
                <span class="required-star">*</span>
              </label>
              <select
                id="class_number"
                v-model.number="form.class_number"
                class="form-input form-select font-mono"
                required
                @blur="validateField('class_number')"
              >
                <option value="" disabled>Sinfni tanlang</option>
                <option v-for="c in classOptions" :key="c" :value="c">{{ c }}-sinf</option>
              </select>
              <span v-if="errors.class_number" class="field-error">{{ errors.class_number }}</span>
            </div>
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            class="btn-editorial-pill submit-action"
            :disabled="loading"
          >
            <span v-if="loading" class="spinner"></span>
            <span>{{ submitText }}</span>
            <span v-if="!loading">→</span>
          </button>
        </form>
      </div>
    </div>

    <!-- Success Celebration Modal Notification -->
    <transition name="modal-bounce">
      <div v-if="success" class="modal-backdrop">
        <div class="success-modal-card">
          <!-- Animated checkmark ring -->
          <div class="success-icon-wrap">
            <div class="pulse-ring"></div>
            <div class="icon-circle">
              <svg viewBox="0 0 24 24" class="check-svg" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </div>
          </div>

          <div class="modal-badge">MUVAFFAQIYATLI RO'YXATDAN O'TINGIZ!</div>

          <h2 class="modal-title">
            Tabriklaymiz, arizangiz <span class="gold-text">qabul qilindi!</span>
          </h2>

          <p class="modal-desc">
            Siz viloyat matematika olimpiadasida muvaffaqiyatli ro'yxatdan o'tdingiz. Tez orada koordinatormiz siz bilan bog'lanadi.
          </p>

          <div class="modal-id-box">
            <span class="id-label">ISHTIROKCHI ID RAQAMI</span>
            <span class="id-number font-mono">#{{ participantId }}</span>
          </div>

          <!-- Progress Countdown Bar -->
          <div class="redirect-indicator">
            <span>{{ countdown }} soniyadan so'ng bosh sahifaga yo'naltiriladi...</span>
            <div class="progress-bar-bg">
              <div class="progress-bar-fill" :style="{ width: `${(countdown / 4) * 100}%` }"></div>
            </div>
          </div>

          <button @click="goToHomeImmediately" class="btn-editorial-pill home-redirect-btn">
            <span>Bosh sahifaga o'tish</span>
            <span>→</span>
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, onUnmounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import confetti from "canvas-confetti"
import { registerParticipant } from "../services/api.js"

const route = useRoute()
const router = useRouter()
const classOptions = [5, 6, 7]

const form = reactive({
  full_name: "",
  phone: "",
  class_number: "",
})

const errors = reactive({})
const loading = ref(false)
const success = ref(false)
const serverError = ref("")
const participantId = ref(null)
const countdown = ref(4)
let timerId = null

onMounted(() => {
  if (route.query.phone) {
    form.phone = route.query.phone
    formatPhone()
  }
})

onUnmounted(() => {
  if (timerId) clearInterval(timerId)
})

const submitText = computed(() => {
  return loading.value ? "Yuborilmoqda..." : "Ro'yxatdan o'tishni yakunlash"
})

function formatPhone() {
  let v = form.phone.replace(/[^\d+]/g, "")
  if (!v.startsWith("+")) {
    if (v.startsWith("998")) v = "+" + v
    else if (v.startsWith("8") || v.startsWith("9")) v = "+998" + v
  }
  form.phone = v
}

function validateField(field) {
  delete errors[field]
  const v = form[field]

  switch (field) {
    case "full_name":
      if (!v || v.trim().length < 3) errors[field] = "To'liq ism-familiyangizni kiriting"
      break
    case "phone":
      if (!v) { errors[field] = "Telefon raqami majburiy"; break }
      {
        const cleaned = v.replace(/[^\d+]/g, "")
        if (!/^\+?998\d{9}$/.test(cleaned)) errors[field] = "Format: +998901234567"
      }
      break
    case "class_number":
      if (!v) errors[field] = "Sinfingizni tanlang"
      break
  }
  return !errors[field]
}

function validateAll() {
  const fields = ["full_name", "phone", "class_number"]
  let valid = true
  for (const f of fields) {
    if (!validateField(f)) valid = false
  }
  return valid
}

function launchCelebration() {
  try {
    // Left burst
    confetti({
      particleCount: 80,
      angle: 60,
      spread: 60,
      origin: { x: 0.1, y: 0.7 },
      colors: ['#e5b22e', '#f3cf7a', '#10b981', '#3b82f6', '#ffffff']
    })
    // Right burst
    confetti({
      particleCount: 80,
      angle: 120,
      spread: 60,
      origin: { x: 0.9, y: 0.7 },
      colors: ['#e5b22e', '#f3cf7a', '#10b981', '#3b82f6', '#ffffff']
    })
    // Center star burst
    setTimeout(() => {
      confetti({
        particleCount: 60,
        spread: 100,
        origin: { y: 0.5 },
        colors: ['#e5b22e', '#10b981', '#ffffff']
      })
    }, 250)
  } catch (e) {
    console.log(e)
  }
}

function goToHomeImmediately() {
  if (timerId) clearInterval(timerId)
  router.push("/")
}

async function handleSubmit() {
  serverError.value = ""
  if (!validateAll()) return
  if (loading.value) return

  loading.value = true

  try {
    const payload = {
      full_name: form.full_name.trim(),
      phone: form.phone.replace(/[^\d+]/g, ""),
      class_number: Number(form.class_number),
    }

    const result = await registerParticipant(payload)
    participantId.value = result.id
    success.value = true

    // Launch celebration confetti
    launchCelebration()

    // Countdown and redirect
    countdown.value = 4
    timerId = setInterval(() => {
      countdown.value--
      if (countdown.value <= 0) {
        clearInterval(timerId)
        router.push("/")
      }
    }, 1000)
  } catch (err) {
    if (err.fieldErrors) {
      for (const [key, msg] of Object.entries(err.fieldErrors)) {
        errors[key] = msg
      }
    }
    serverError.value = err.message || "Xatolik yuz berdi"
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register-page {
  min-height: 100vh;
  position: relative;
  background-color: var(--bg-deep);
  padding: calc(var(--header-height) + 40px) 0 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.register-container {
  width: 100%;
  max-width: 620px;
  position: relative;
  z-index: 2;
}

.editorial-card-wrapper {
  background: rgba(255, 255, 255, 0.025);
  border: 1px solid var(--border-medium);
  border-radius: 18px;
  padding: 44px;
  width: 100%;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
}

.back-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  color: var(--text-secondary);
  margin-bottom: 24px;
  transition: color 0.2s ease;
}

.back-link:hover {
  color: var(--gold);
}

.form-header {
  margin-bottom: 32px;
}

.form-title {
  font-size: clamp(1.8rem, 3.5vw, 2.4rem);
  font-weight: 700;
  letter-spacing: -0.03em;
  color: #ffffff;
  margin-bottom: 8px;
  line-height: 1.2;
}

.form-desc {
  font-size: 0.95rem;
  color: var(--text-secondary);
  line-height: 1.6;
}

/* Error Banner */
.error-banner {
  padding: 14px 18px;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: 10px;
  margin-bottom: 24px;
  font-size: 0.88rem;
  color: #fca5a5;
}

/* Register Form */
.register-form {
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.form-row {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 18px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  gap: 4px;
}

.required-star {
  color: var(--gold);
}

.form-input {
  width: 100%;
  height: 50px;
  padding: 0 16px;
  background: rgba(255, 255, 255, 0.035);
  border: 1px solid var(--border-medium);
  border-radius: 10px;
  color: #ffffff;
  font-size: 0.95rem;
  font-family: var(--font-sans);
  transition: all 0.2s ease;
  outline: none;
}

.form-input::placeholder {
  color: var(--text-dim);
  font-size: 0.88rem;
}

.form-input:focus {
  border-color: var(--gold);
  background: rgba(255, 255, 255, 0.06);
  box-shadow: 0 0 18px rgba(229, 178, 46, 0.18);
}

.form-select {
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%23e5b22e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 14px center;
  padding-right: 36px;
}

.form-select option {
  background: #0d0a1c;
  color: #ffffff;
}

.form-group.error .form-input {
  border-color: #ef4444;
}

.field-error {
  font-size: 0.75rem;
  color: #f87171;
  font-family: var(--font-sans);
}

.submit-action {
  width: 100%;
  justify-content: center;
  height: 52px;
  font-size: 1rem;
  margin-top: 10px;
}

.spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(7, 9, 19, 0.3);
  border-top-color: #070913;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Success Modal Notification */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(3, 4, 10, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  padding: 20px;
}

.success-modal-card {
  background: linear-gradient(135deg, rgba(20, 16, 38, 0.95), rgba(10, 8, 20, 0.98));
  border: 1px solid rgba(229, 178, 46, 0.4);
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7), 0 0 40px rgba(229, 178, 46, 0.2);
  border-radius: 20px;
  padding: 44px 36px;
  max-width: 480px;
  width: 100%;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  animation: modalPop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.success-icon-wrap {
  position: relative;
  width: 76px;
  height: 76px;
  margin-bottom: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pulse-ring {
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  border: 2px solid rgba(16, 185, 129, 0.5);
  animation: pulseEffect 2s ease-out infinite;
}

.icon-circle {
  width: 68px;
  height: 68px;
  border-radius: 50%;
  background: linear-gradient(135deg, #10b981, #059669);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 24px rgba(16, 185, 129, 0.4);
}

.check-svg {
  width: 36px;
  height: 36px;
}

.modal-badge {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.15em;
  color: #10b981;
  font-weight: 700;
  margin-bottom: 12px;
}

.modal-title {
  font-size: 1.6rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 12px;
  line-height: 1.3;
}

.gold-text {
  color: var(--gold);
}

.modal-desc {
  font-size: 0.92rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 24px;
}

.modal-id-box {
  background: rgba(229, 178, 46, 0.08);
  border: 1px solid rgba(229, 178, 46, 0.25);
  border-radius: 12px;
  padding: 14px 28px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-bottom: 24px;
  width: 100%;
}

.id-label {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  letter-spacing: 0.1em;
  color: var(--text-dim);
}

.id-number {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--gold);
}

.redirect-indicator {
  width: 100%;
  margin-bottom: 22px;
  font-size: 0.8rem;
  color: var(--text-dim);
  font-family: var(--font-mono);
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.progress-bar-bg {
  width: 100%;
  height: 4px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 99px;
  overflow: hidden;
}

.progress-bar-fill {
  height: 100%;
  background: var(--gold);
  border-radius: 99px;
  transition: width 1s linear;
}

.home-redirect-btn {
  width: 100%;
  justify-content: center;
  height: 48px;
  font-size: 0.95rem;
}

@keyframes pulseEffect {
  0% {
    transform: scale(0.9);
    opacity: 0.8;
  }
  100% {
    transform: scale(1.4);
    opacity: 0;
  }
}

@keyframes modalPop {
  0% {
    opacity: 0;
    transform: scale(0.9) translateY(20px);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

.modal-bounce-enter-active,
.modal-bounce-leave-active {
  transition: opacity 0.3s ease;
}

.modal-bounce-enter-from,
.modal-bounce-leave-to {
  opacity: 0;
}

@media (max-width: 640px) {
  .editorial-card-wrapper {
    padding: 28px 18px;
  }
  .form-row {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  .success-modal-card {
    padding: 32px 20px;
  }
}
</style>

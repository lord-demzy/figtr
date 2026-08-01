import { useState, useEffect } from "react";
import { cn } from "@/lib/utils";

type ToastVariant = "default" | "destructive";

interface ToastProps {
  id: string;
  title?: string;
  description?: string;
  variant?: ToastVariant;
}

const listeners: ((toasts: ToastProps[]) => void)[] = [];
let toastQueue: ToastProps[] = [];

const toast = ({
  title,
  description,
  variant = "default",
}: Omit<ToastProps, "id">) => {
  const id = Math.random().toString(36).slice(2, 9);
  const newToast: ToastProps = { id, title, description, variant };
  toastQueue = [...toastQueue, newToast];
  listeners.forEach((listener) => listener(toastQueue));

  setTimeout(() => {
    toastQueue = toastQueue.filter((t) => t.id !== id);
    listeners.forEach((listener) => listener(toastQueue));
  }, 5000);
};

const dismiss = (id: string) => {
  toastQueue = toastQueue.filter((t) => t.id !== id);
  listeners.forEach((listener) => listener(toastQueue));
};

function useToast() {
  const [state, setState] = useState<ToastProps[]>([]);

  useEffect(() => {
    listeners.push(setState);
    return () => {
      const index = listeners.indexOf(setState);
      if (index > -1) listeners.splice(index, 1);
    };
  }, []);

  return {
    toasts: state,
    toast,
    dismiss,
  };
}

function Toaster() {
  const { toasts, dismiss } = useToast();

  if (toasts.length === 0) return null;

  return (
    <div
      data-slot="toaster"
      className="fixed top-4 right-4 z-[100] flex flex-col gap-2 w-full max-w-sm"
    >
      {toasts.map((t) => (
        <div
          key={t.id}
          className={cn(
            "pointer-events-auto flex items-start justify-between rounded-lg border p-3 text-sm shadow-lg",
            "bg-popover text-popover-foreground",
            t.variant === "destructive" &&
              "border-destructive bg-destructive text-destructive-foreground"
          )}
        >
          <div className="grid gap-1">
            {t.title && <div className="font-semibold">{t.title}</div>}
            {t.description && <div className="text-xs opacity-90">{t.description}</div>}
          </div>
          <button
            onClick={() => dismiss(t.id)}
            className="ml-2 rounded-md p-1 opacity-60 hover:opacity-100"
          >
            ×
          </button>
        </div>
      ))}
    </div>
  );
}

export { toast, Toaster, useToast, dismiss };

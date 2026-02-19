import numpy as np
import nanosurf as nsf

path = r"C:\Users\caspa\OneDrive\Documents\University\Year 3\Laboratory work\Sem 2 - STM\Maisie images(just for code testing)#\Image00194.nid"

nid = nsf.util.nid_reader.NIDFileReader()
assert nid.read(path)

def peek(obj, name, max_items=30):
    print(f"\n=== {name} ===")

    # dict-like
    if hasattr(obj, "keys"):
        ks = list(obj.keys())
        print("keys:", ks[:max_items], ("...(+more)" if len(ks) > max_items else ""))
        for k in ks[:min(10, len(ks))]:
            try:
                arr = np.asarray(obj[k])
                print(f"  {k!r}: shape={arr.shape} dtype={arr.dtype} min/max={np.nanmin(arr)}/{np.nanmax(arr)}")
            except Exception as e:
                print(f"  {k!r}: (could not summarize) {e}")
        return

    # attribute-like
    attrs = [a for a in dir(obj) if not a.startswith("_")]
    print("attrs:", attrs[:max_items], ("...(+more)" if len(attrs) > max_items else ""))

# Explore spectroscopy segments
peek(nid.data.spectroscopy, "nid.data.spectroscopy")
peek(nid.data.spectroscopy.forward, "nid.data.spectroscopy.forward")
peek(nid.data.spectroscopy.backward, "nid.data.spectroscopy.backward")
peek(nid.data.spectroscopy.forward_pause, "nid.data.spectroscopy.forward_pause")
peek(nid.data.spectroscopy.backward_pause, "nid.data.spectroscopy.backward_pause")

# Explore spectrum subtypes
peek(nid.data.spectrum, "nid.data.spectrum")
peek(nid.data.spectrum.sweep, "nid.data.spectrum.sweep")
peek(nid.data.spectrum.fit, "nid.data.spectrum.fit")
peek(nid.data.spectrum.fft, "nid.data.spectrum.fft")
peek(nid.data.spectrum.sweep_sho, "nid.data.spectrum.sweep_sho")
spec = nid.data.spectroscopy.forward

I = np.asarray(spec["Tip Current"])[0, :]
V = np.asarray(spec["Tip voltage"])[0, :]

print(I.shape, V.shape)
import numpy as np
import matplotlib.pyplot as plt

spec = nid.data.spectroscopy.forward

I = np.asarray(spec["Tip Current"])[0, :]
V = np.asarray(spec["Tip voltage"])[0, :]

plt.plot(V, I)
plt.xlabel("Tip voltage (V)")
plt.ylabel("Tip Current (A)")
plt.title("STM I–V Forward Sweep")
plt.show()
